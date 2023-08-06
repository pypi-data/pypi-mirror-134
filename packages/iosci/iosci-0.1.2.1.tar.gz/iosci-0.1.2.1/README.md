# ios 自动修改podfile组件版本号，支持批量修改
如果podfile中不存在组件aaa，则添加到podfile第一个target中,如果有:configurations=>['Debug']则保留
f_podfile = '/Users/lch/Desktop/Podfile'
update_component_with_newversion(f_podfile, ['aaa:1.0','bbb:2.0'])

## podfile转为model对象
      podfile = '/Users/lch/Documents/z/proj/Podfile'
      podfile_model = CIPodfileParse.getPodfileModel(podfile)
      print(podfile_model)

## 验证字符串是不是版本号
    isversion = CIVersionManager.isVersion('1.1.2')
    print(isversion)

## 执行shell脚本
    # os_system('cat aaa')
    (status, msg) = os_popen('xcodebuild  aaa > /dev/null')
    print(status)
    print(msg)