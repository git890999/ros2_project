from setuptools import find_packages, setup

package_name = 'my_ros2_keyboard'

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
    maintainer='issa2',
    maintainer_email='issa2@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'server = my_ros2_keyboard.server:main',
        'client = my_ros2_keyboard.client:main',
        ],
    },
)
