// 前端筛选日志直接提交记录生成文件
// node tagLog.js v2.7.7 v2.7.8 调用命令
const childProcess = require('child_process');
const fs = require('fs');
let startDate = process.argv[2];
let endDate = process.argv[3];
const branch = process.argv[4] || 'master';
if (!startDate || !endDate) {
    throw new Error('命令格式不对, 应该为node log.js startDate(2020-05-01) endDate(2020-06-18)')
} else {
    startDate = startDate + ' 00:00:00';
    endDate = endDate + ' 23:59:59'
}
const filePath = `./日志提交记录.csv`;
// console.log('process.argv', process.argv)
function createCsv(list) {
    // 生成表头 ( \ufeff --> 防止乱码 )
    var csvContent = '\ufeff作者,';
    csvContent += '提交信息,';
    csvContent += '提交日期\n';
    if (fs.existsSync(filePath)) {
        fs.unlinkSync(filePath);
    }

    // 生成内容 \n下一行
    list.forEach((item, index) => {
        csvContent += item[0] + ',';
        csvContent += item[1] + ',';
        csvContent += item[2] + '\n';
    })

    // 生成csv文件
    fs.writeFile(filePath, csvContent, function (err) {
        if (err) console.log(err, '---->csv<---')
    })

}

childProcess.exec(`git checkout ${branch}`, (error, stdout, status, output) => {
    if (error) console.log(error)
    childProcess.exec(`git fetch origin`, (error) => {
        if (error) console.log(error)
        // git log --pretty=oneline tagA...tagB
        childProcess.exec(`git log --pretty=format:"%cn=>=>=>%s=>=>=>%cd" --after="${startDate}" --before="${endDate}"`, { encoding: 'utf8' }, (error, stdout, status, output) => {
            if (error) console.log(error)
            const array = stdout.split(/\n/)
                                            .filter(item => {
                                                return (item.indexOf('合并分支') === -1 && item.indexOf('Merge branch') === -1 && item.indexOf('删除 ') === -1)
                                                 && (item.indexOf('ganghuang_wu') > -1 || item.indexOf('wgh') > -1)
                                            })
                                            .map(item => { return item.split('=>=>=>') })
            console.log('array', array);
            createCsv(array)
            console.log('生成成功')
        });
    })
})

// git log --after="2018-05-21 00:00:00" --before="2018-05-25 23:59:59"


