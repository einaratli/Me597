from setuptools import find_packages, setup

package_name = 'task_2'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='me597',
    maintainer_email='einaratligudna@outlook.com',
    description='description=Publisher/subscriber and service nodes for joint data',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_publisher = task_2.publisher:main',
            'joint_subscriber = task_2.subscriber:main',
            'joint_server = task_2.service:main',
            'joint_client = task_2.client:main'
    ],
},
)
