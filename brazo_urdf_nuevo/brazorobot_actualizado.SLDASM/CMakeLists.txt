<<<<<<< HEAD:src/BRAZO_URDF_V3/CMakeLists.txt
cmake_minimum_required(VERSION 2.8.3)

project(BRAZO_URDF_V3)

find_package(catkin REQUIRED COMPONENTS
	message_generation
	roscpp
	rospy
	std_msgs
	geometry_msgs
	urdf
	xacro
	message_generation
)

catkin_package(
	CATKIN_DEPENDS
	geometry_msgs
	roscpp
	rospy
	std_msgs
)


find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
=======
cmake_minimum_required(VERSION 2.8.3)

project(brazorobot_actualizado.SLDASM)

find_package(catkin REQUIRED)

catkin_package()

find_package(roslaunch)

foreach(dir config launch meshes urdf)
	install(DIRECTORY ${dir}/
		DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)
>>>>>>> 0ac9abf2ff55e3c3c5f4f532b7a559d4fe31e4af:brazo_urdf_nuevo/brazorobot_actualizado.SLDASM/CMakeLists.txt
