from setuptools import find_packages, setup

package_name = 'my_ros2_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='issa2',
    maintainer_email='issa2@todo.todo',
    description='Package ROS 2 contenant des publishers/subscribers et un service client/serveur',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature = my_ros2_package.temperature:main',
            'humidite = my_ros2_package.humidite:main',
            'co2 = my_ros2_package.co2:main',
            'chauffage = my_ros2_package.chauffage:main',
            'fenetre = my_ros2_package.fenetre:main',
            'lumiere = my_ros2_package.lumiere:main',
            'stores = my_ros2_package.stores:main',
            'alarme = my_ros2_package.alarme:main',
            'client = my_ros2_package.my_ros2_keyboard.client:main',
            'serveur = my_ros2_package.my_ros2_keyboard.server:main',
        ],
    },
)

