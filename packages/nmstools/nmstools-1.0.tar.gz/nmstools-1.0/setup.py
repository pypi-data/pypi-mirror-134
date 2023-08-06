import setuptools

requirements = ['numpy']

setuptools.setup(
    name="nmstools",                                     # 包的分发名称，使用字母、数字、_、-
    version="1.0",                                        # 版本号, 版本号规范：https://www.python.org/dev/peps/pep-0440/
    author="stjuliet",                                       # 作者名字
    author_email="andy19966212@126.com",                      # 作者邮箱
    description="PyPI Tutorial",                            # 包的简介描述
    license='MIT-0',
    url="https://github.com/stjuliet",                           # 项目开源地址
    packages=setuptools.find_packages(),                    # 如果项目由多个文件组成，我们可以使用find_packages()自动发现所有包和子包，而不是手动列出每个包，在这种情况下，包列表将是example_pkg
    install_requires=requirements,  # 依赖的包
    python_requires='>=3.5'
)
