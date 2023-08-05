from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="CsuSort",  # 这里是pip项目发布的名称
    version="1.0.6",  # 版本号，数值大的会优先被pip
    keywords=["pip", "sort"],
    description="person or car",
    # long_description="",
    license="MIT Licence",
    author="csu_ywj",
    # author_email="888@qq.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=["Keras", "tensorflow-gpu", "numpy", "opencv-python", "scikit-learn", "scipy", "Pillow", "torch", "torchvision"]
)
