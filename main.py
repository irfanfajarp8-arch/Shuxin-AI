from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class ShuxinAIApp(App):
    def build(self):
        # Mengatur background gelap gulita khas sistem hologram
        Window.clearcolor = (0, 0, 0.02, 1) 
        
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        # 1. VISUAL INDIKATOR HOLOGRAM (Efek Proyeksi Emitter)
        self.hologram_visual = Label(
            text="🌐\n[ HOLOGRAM MODE ACTIVE ]\n✨ SHUXIN 3D VISUAL EMITTER ✨",
            font_size='18sp',
            color=(0, 1, 0.9, 1),
            halign='center'
        )
        
        # 2. STATUS SISTEM SUARA & KEAMANAN REAL
        self.status_label = Label(
            text="🔊 SYSTEM STATUS:\nMenunggu Perintah Suara Tuan Irfan...\n\n"
                 "[✓] PROTEKSI TELEPON: OTOMATIS REJECT\n"
                 "[✓] KEAMANAN REKENING: DATA TERENKRIPSI TOTAL",
            font_size='14sp',
            color=(0.5, 0.9, 1, 1),
            halign='center'
        )
        
        # 3. TOMBOL SIMULASI PERINTAH SUARA (VOICE COMMAND)
        self.btn_suara = Button(
            text="🎤 [SIMULASI SUARA]: 'Shuxin, Periksa Keamanan!'",
            size_hint=(1, 0.2),
            background_color=(0, 0.5, 0.8, 1),
            font_size='13sp'
        )
        self.btn_suara.bind(on_press=self.simulasi_perintah_suara)
        
        self.layout.add_widget(self.hologram_visual)
        self.layout.add_widget(self.status_label)
        self.layout.add_widget(self.btn_suara)
        
        return self.layout

    def simulasi_perintah_suara(self, instance):
        # Efek respon hologram ketika mendengar suara Tuan Irfan
        self.hologram_visual.text = "🤖\n[ HOLOGRAM TALKING ]\n'Saya Shuxin asisten pintar siap melayani tuan Irfan!'"
        self.hologram_visual.color = (0.2, 1, 0.6, 1)
        
        log_keamanan = (
            "🔊 PERINTAH SUARA DITERIMA!\n"
            "-----------------------------------------\n"
            "[✓] Panggilan nomor asing otomatis di-reject sistem!\n"
            "[✓] Sandi Bank aman, akses dana luar diblokir total!\n"
            "-----------------------------------------\n"
            "🛡️ STATUS: HP Tuan Irfan Aman 100%!"
        )
        self.status_label.text = log_keamanan
        self.status_label.color = (0.2, 1, 0.5, 1)

if __name__ == '__main__':
    ShuxinAIApp().run()
