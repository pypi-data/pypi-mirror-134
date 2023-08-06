import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "pahud-cdktf-aws-eks",
    "version": "0.3.0",
    "description": "CDKTF construct library for Amazon EKS",
    "license": "Apache-2.0",
    "url": "https://github.com/pahud/cdktf-aws-eks",
    "long_description_content_type": "text/markdown",
    "author": "Pahud Hsieh<pahudnet@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/pahud/cdktf-aws-eks"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "pahud_cdktf_aws_eks",
        "pahud_cdktf_aws_eks._jsii"
    ],
    "package_data": {
        "pahud_cdktf_aws_eks._jsii": [
            "cdktf-aws-eks@0.3.0.jsii.tgz"
        ],
        "pahud_cdktf_aws_eks": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "cdktf-cdktf-provider-aws>=3.0.1, <4.0.0",
        "cdktf-cdktf-provider-kubernetes>=0.4.29, <0.5.0",
        "cdktf>=0.8.1, <0.9.0",
        "constructs>=10.0.0, <11.0.0",
        "jsii>=1.39.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
