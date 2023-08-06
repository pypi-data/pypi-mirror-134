from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="CsuOpenpose",  # 这里是pip项目发布的名称
    version="1.0.13",  # 版本号，数值大的会优先被pip
    keywords=["pip", "openpose"],
    description="pose",
    license="MIT Licence",
    author="csu_ywj",
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    platforms="any",
    install_requires=["numpy==1.19.2", "matplotlib==3.3.4", "opencv-python==4.5.5.62", "scipy==1.5.4",
                      "scikit-image==0.17.2", "tqdm==4.62.3"]
)