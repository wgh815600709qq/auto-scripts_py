// 前端tag直接提交记录生成文件
// node tagLog.js v2.7.7 v2.7.8 调用命令
const childProcess = require('child_process');
const fs = require('fs');
const tagA = process.argv[2];
const tagB = process.argv[3];
if (!tagA || !tagB) {
    throw new Error('命令格式不对, 应该为node tagLog.js tag1 tag2')
}
const filePath = `./tag${tagB}前端代码提交记录.csv`;
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
  fs.writeFile(filePath, csvContent, function(err){
    if (err) console.log(err, '---->csv<---')
  })

}

childProcess.exec(`git checkout master`, (error, stdout, status, output) => {
  if (error) console.log(error)
  childProcess.exec(`git fetch origin`, (error) => {
    if (error) console.log(error)
    // git log --pretty=oneline tagA...tagB
    childProcess.exec(`git log --pretty=format:"%cn=>=>=>%s=>=>=>%cd" ${tagA}...${tagB}`, { encoding: 'utf8' }, (error, stdout, status, output) => {
      if (error) console.log(error)
      const array = stdout.split(/\n/).filter(item => item.indexOf('合并分支 ') === -1).map(item => {return item.split('=>=>=>')})
      createCsv(array)
      console.log(`tag${tagA}至tag${tagB}的提交日志生成成功！生成文件${tagB}.csv`)
    });
  })
})


