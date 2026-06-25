from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.togglebutton import ToggleButton

class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # 카메라 오브젝트 생성 (Play 속성을 활용해 켜고 끎)
        self.camera_obj = Camera(resolution=(640, 480), play=True)
        
        # 카메라 On/Off 토글 버튼
        toggle_btn = ToggleButton(text='Stop Camera', state='down', size_hint_y=0.1)
        toggle_btn.bind(on_press=self.toggle_camera)
        
        layout.add_widget(self.camera_obj)
        layout.add_widget(toggle_btn)
        return layout

    def toggle_camera(self, instance):
        if instance.state == 'down':
            self.camera_obj.play = True
            instance.text = 'Stop Camera'
        else:
            self.camera_obj.play = False
            instance.text = 'Start Camera'

if __name__ == '__main__':
    CameraApp().run()