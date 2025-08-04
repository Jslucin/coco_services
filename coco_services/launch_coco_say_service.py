#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import subprocess

class CocoSayService(Node):
    def __init__(self):
        super().__init__('launch_coco_say_service')
        self.srv = self.create_service(Trigger, '/launch_coco_say', self.launch_callback)
        self.get_logger().info('Servicio /launch_coco_say listo.')

    def launch_callback(self, request, response):
        try:
            subprocess.Popen([
                'bash', '-c',
                'LIBGL_ALWAYS_SOFTWARE=1 ros2 launch coco_dice coco_say.launch.py'
            ])
            response.success = True
            response.message = 'Launch ejecutado correctamente.'
            self.get_logger().info('Launch lanzado.')
        except Exception as e:
            response.success = False
            response.message = f'Error: {e}'
            self.get_logger().error(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = CocoSayService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
