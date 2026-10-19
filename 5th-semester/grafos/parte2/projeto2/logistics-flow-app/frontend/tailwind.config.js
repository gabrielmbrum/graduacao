/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      colors: {
        void: '#0A0E1A',
        panel: '#101828',
        'panel-raised': '#16223A',
        line: '#24304A',
        'line-soft': '#1A2338',
        flow: '#38BDF8',
        saturated: '#FB7185',
        signal: '#F5A524',
        ink: '#E8EDF7',
        muted: '#6B7B99',
      },
      fontFamily: {
        display: ['"Space Grotesk"', 'sans-serif'],
        body: ['"Inter"', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      backgroundImage: {
        blueprint:
          'linear-gradient(rgba(56,189,248,0.05) 1px, transparent 1px), linear-gradient(90deg, rgba(56,189,248,0.05) 1px, transparent 1px)',
        hazard:
          'repeating-linear-gradient(135deg, #F5A524 0, #F5A524 8px, #0A0E1A 8px, #0A0E1A 16px)',
      },
      backgroundSize: {
        grid: '28px 28px',
      },
    },
  },
  plugins: [],
}
