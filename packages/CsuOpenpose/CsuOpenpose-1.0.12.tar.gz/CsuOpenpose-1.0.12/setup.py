from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="CsuOpenpose",  # 这里是pip项目发布的名称
    version="1.0.12",  # 版本号，数值大的会优先被pip
    keywords=["pip", "openpose"],
    description="pose",
    license="MIT Licence",
    author="csu_ywj",
    packages=find_packages(),
    data_files=[],
    include_package_data=True,
    platforms="any",
    install_requires=["numpy", "matplotlib", "opencv-python", "scipy", "scikit-image", "tqdm"]
)