
# 将单个组件的版本号更新到podfile
from iosci.Podfile.CIComponentModel import CIComponentModel
from iosci.xcode.CIPodfileParse import CIPodfileParse


def update_component_to_model(name, version, podfile_model):
    # 组件在podfile在是否存在
    exists = False
    # 找出第一个target
    first_target = []
    # 组件在podfile中存在，更新版本号
    for target in podfile_model:
        if isinstance(target, list):
            if len(first_target) == 0:
                first_target = target

            for component in target:
                if isinstance(component, CIComponentModel):
                    if 'pod \'%s\'' % name == component.name.lstrip():
                        component.version = version
                        exists = True
                        break
    # 组件在podfile中不存在，添加组件到第一个target中
    if not exists:
        if name and version:
            cm = CIComponentModel()
            cm.name = '  pod \'%s\'' % name
            cm.version = version
            first_target.insert(1, cm)
        else:
            raise Exception("名称%s 或者版本号%s 不存在" % (name, version))

# 将最终结果重写到podfile中
def rewrite_to_podfile(podfile_path, podfile_model):
    contents = ''
    # model 转为字符串
    for target in podfile_model:
        if isinstance(target, list):
            for component in target:
                if isinstance(component, CIComponentModel):
                    # 有版本号直接用版本号，没版本号则原样拼出
                    if component.version:
                        # configurations 的配置，在什么情况下都应该保留
                        if component.configurations:
                            pod = "%s, %s , %s\n" % (component.name, component.version, component.configurations)
                        else:
                            pod = "%s, %s \n" % (component.name, component.version)
                    else:
                        pod = component.name
                        if component.git:
                            pod += ", %s" % component.git
                        if component.branch:
                            pod += ", %s" % component.branch
                        if component.other:
                            pod += ", %s" % component.other
                        # configurations 的配置，在什么情况下都应该保留
                        if component.configurations:
                            pod += ", %s" % component.configurations
                    contents += pod
                else:
                    contents += component
        else:
            contents += target
    with open(podfile_path, 'w+') as podfile:
        podfile.write(contents)

# 更新podfile中的组件指向新版本号
# 传过来的参数是：[组件名:版本号]
def update_component_with_newversion(podfile_path, components):
    print('获取到参数为：', podfile_path, components)
    # 读取podfile文件，翻译为对象
    podfile_model = CIPodfileParse.getPodfileModel(podfile_path)
    # 把传过来的组件更新到对象中
    for component in components:
        _componentSeg = component.split(':')
        if len(_componentSeg) == 2:
            name = _componentSeg[0]
            version = _componentSeg[1]
            update_component_to_model(name, "'%s'" % version, podfile_model)
        else:
            raise Exception("传过来的组件格式不对 %s" % component)

    # 把新的内容写入到podfile中
    rewrite_to_podfile(podfile_path, podfile_model)


if __name__ == '__main__':
    f_podfile = '/Users/lch/Desktop/Podfile'
    update_component_with_newversion(f_podfile, ['aaa:1.0','bbb:2.0'])
