import pytest

# 初始化钩子，注册标签
def pytest_configure(config):
    config.addinivalue_line( # 注册名为tags的标签
        "markers","tags"
    )


# 初始化钩子，自定义命令行参数
def pytest_addoption(parser):
    parser.addoption("--tags", action="store", default="",
                     help="指定运行测试用例的标签，如：smoke")


# 收集钩子，在执行收集后调用，在这里面把没打标签的用例给过滤掉了
def pytest_collection_modifyitems(items,session):
    opt_tags = session.config.getoption("tags") #获取命令行参数tag的值
    if opt_tags: # 如果运行时候指定了tags，比如指定的是--tags=smoke
        opt_tags_list = opt_tags.split(",")
        skip_marker = pytest.mark.skip(reason=f'Run only tagged {opt_tags_list}')
        for i in items: # 遍历所有的测试用例，检查每个用例的tags标记里面有没有包含smoke的值，如果没有就跳过了
            tags_maker = i.get_closest_marker("tags")
            tags = None
            if tags_maker: tags = tags_maker.args[0]
            if (
                    tags is None
                    or any([k in opt_tags_list for k in tags]) == False
            ):
                i.add_marker(skip_marker)