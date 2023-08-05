const createWindowsInstaller = require('electron-winstaller').createWindowsInstaller
const path = require('path')

getInstallerConfig()
  .then(createWindowsInstaller)
  .catch((error) => {
    console.error(error.message || error)
    process.exit(1)
  })

function getInstallerConfig () {
  console.log('Creating windows installer')
  const rootPath = path.join('./')
  const outPath = path.join(rootPath, 'release-builds')

  return Promise.resolve({
    appDirectory: path.join(rootPath, 'Stor-win32-x64'),
    authors: 'Stor Network',
    version: process.env.STOR_INSTALLER_VERSION,
    noMsi: true,
    iconUrl: 'https://raw.githubusercontent.com/Stor-Network/stor-blockchain/master/electron-react/src/assets/img/stor.ico',
    outputDirectory: path.join(outPath, 'windows-installer'),
    certificateFile: 'win_code_sign_cert.p12',
    certificatePassword: process.env.WIN_CODE_SIGN_PASS,
    exe: 'Stor.exe',
    setupExe: 'StorSetup-' + process.env.STOR_INSTALLER_VERSION + '.exe',
    setupIcon: path.join(rootPath, 'src', 'assets', 'img', 'stor.ico')
  })
}
