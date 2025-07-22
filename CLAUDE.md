# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ini adalah project presentasi webinar tentang Computer Vision untuk frontend developer pemula. Materinya didesain khusus untuk developer yang belum pernah menyentuh AI/ML tapi pengen tahu gimana cara kerja fitur-fitur "pintar" di aplikasi yang sering kita lihat.

Project ini berbentuk HTML presentation yang bisa dijalankan langsung di browser, cocok banget buat yang udah familiar dengan frontend development.

## Struktur Project

- `pertemuan-1.html` - File presentasi utama (25 slides) berisi pengenalan computer vision dari sudut pandang frontend
- `index.html` - Masih kosong, kemungkinan untuk landing page
- `.vscode/settings.json` - Setting Live Server port 5501

## Cara Menjalankan

Karena ini pure HTML/CSS/JS, gampang banget:

```bash
# Pakai Live Server VS Code extension (port 5501 udah di-set)
# Atau buka langsung pertemuan-1.html di browser

# No npm install, no build process - langsung jalan!
```

## Fitur Presentasi

### Navigasi Slide
- Keyboard: Arrow keys, Space, Home, End (kayak PowerPoint)
- Button: Tombol Previous/Next
- Counter: Slide ke berapa dari total berapa

### Demo Interaktif (Simulasi)
Yang menarik dari presentasi ini adalah ada demo-demo yang mensimulasikan bagaimana computer vision bekerja:
- **Image Classification Demo**: Upload gambar → kasih label (misal: "ini kucing")
- **Object Detection Demo**: Deteksi multiple objek dengan kotak pembatas
- **Teachable Machine Simulation**: Simulasi training model tanpa coding
- **YOLO Detection**: Demo real-time object detection

Ini bagus banget buat frontend developer yang pengen paham konsep tanpa harus deep dive ke algoritma ML yang ribet.

## Content Structure (Frontend Perspective)

1. **Pengenalan Computer Vision**: Apa itu CV dalam konteks web development
2. **3 Tugas Utama CV**: Classification, Detection, Segmentation (dijelaskan dengan analogi frontend)
3. **Aplikasi di Web**: Dari face filters di Instagram sampai product search
4. **Tools untuk Frontend**: Teachable Machine, ML5.js, TensorFlow.js
5. **Implementasi Praktis**: Gimana integrate CV ke web app
6. **Career Path**: Peluang untuk frontend developer masuk ke AI space

## Tech Stack

- **Pure HTML/CSS/JS**: No framework, mudah dimodifikasi
- **Responsive Design**: CSS Grid + Flexbox (familiar buat frontend dev)
- **Interactive JS**: Event handling, DOM manipulation, animations
- **Clean Code**: Struktur yang rapih, mudah dipahami

## Cara Modifikasi Slide

Sebagai frontend developer, struktur ini pasti familiar:

```html
<div class="slide">
  <h2>Judul Slide</h2>
  <div class="content">
    <!-- Konten slide di sini -->
  </div>
</div>
```

- Setiap slide adalah div dengan class "slide"
- CSS ada di dalam `<style>` tag (bisa dipindah ke file terpisah)
- JavaScript demo functions ada di `<script>` tag di bawah
- Tambah slide baru: copy struktur yang ada, update counter

## CSS Classes Penting

- `.slide` - Container utama slide
- `.section-box` - Box untuk pengelompokan konten
- `.card` - Card component untuk info
- `.grid-2`, `.grid-3` - Layout grid
- `.highlight-box` - Box untuk highlight info penting

## Deployment

Sama kayak static site biasa:
- GitHub Pages ✅
- Netlify ✅  
- Vercel ✅
- Surge ✅
- Bahkan bisa upload ke hosting biasa

## Tips untuk Frontend Developer

1. **Fokus ke Implementation**: Materinya lebih ke "gimana pakai" daripada "gimana cara kerjanya"
2. **Practical Examples**: Banyak contoh real-world yang relevan dengan web dev
3. **No-Code Tools**: Pengenalan tools yang gak perlu coding ML dari scratch
4. **Web Integration**: Gimana cara integrate CV features ke existing web app
5. **Progressive Learning**: Dari yang sederhana dulu, baru ke yang kompleks