from setuptools import setup
readme = open('README.rst', 'r')
README_TEXT = readme.read()
readme.close()
setup(
    name='pytest-bugtong-tag',
    url='https://github.com/bugtong',
    version='1.0.0',
    author="bugtong",
    author_email='tj@111.com',
    description='pytest-bugtong-tag is a plugin for pytest',
    long_description=README_TEXT,
    classifiers=[
        'Framework :: Pytest',
        'Programming Language :: Python',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3.7',
    ],
    license='proprietary',
    py_modules=['pytest_bugtong_tag'],#需要打包的模块
    keywords=[
        'pytest', 'py.test', 'pytest-bugtong-tag',
    ],

    install_requires=[
        'pytest'
    ],
    entry_points={ # entry_points是用来支持动态发现服务和插件的
        'pytest11': [ # 登记为pytest插件，pytest通过查找pytest11入口点来识别自己的插件
            'bugtong-tag = pytest_bugtong_tag',
        ]
    }
)