import setuptools
 
setuptools.setup(
    # 项目的名称
    name="splt",
    #项目的版本
    version="2.0",
    # 项目的作者
    author="高乐喆",
    # 作者的邮箱
    author_email="gaolezhe@oulook.com",
    # 项目描述
    description="本函数会要求您输入字符串的长度及字符串本身（只适用于中文字符），本程序将会将这个字符串逐字分开",
    # 项目的长描述
    long_description="本函数会要求您输入字符串的长度及字符串本身（只适用于中文字符），本程序将会将这个字符串逐字分开",
    # 以哪种文本格式显示长描述
    long_description_content_type="text/markdown",  # 所需要的依赖 
    install_requires=[],  # 比如["flask>=0.10"]
    # 项目主页
    url="https://www.baidu.com",
    # 项目中包含的子包，find_packages() 是自动发现根目录中的所有的子包。
    packages=setuptools.find_packages(),
    # 其他信息，这里写了使用 Python3，MIT License许可证，不依赖操作系统。
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
