/**
 * Tokens de design — "Console de Roteamento"
 * Paleta inspirada em NOC (Network Operations Center) / osciloscópio,
 * já que o produto é um simulador técnico de resiliência de rede.
 */
/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#0A0E13",       // fundo principal do console
        panel: "#121820",     // painéis / cartões
        panel2: "#0E1319",    // painel levemente mais escuro (canvas)
        line: "#223040",      // hairlines / bordas
        "line-soft": "#1A2530",
        hi: "#E8EEF3",         // texto principal
        mid: "#8CA0B3",        // texto secundário
        dim: "#576776",        // texto terciário / desabilitado
        signal: "#4FD8C4",     // caminho primário (ciano sinal de fibra)
        redundant: "#9B8CFF",  // caminho redundante (violeta)
        tertiary: "#E8B75E",   // terceiro caminho (âmbar)
        alert: "#FF6B5E",      // falha / corte / desconectado
      },
      fontFamily: {
        mono: ["'JetBrains Mono'", "ui-monospace", "SFMono-Regular", "monospace"],
        sans: ["'IBM Plex Sans'", "ui-sans-serif", "system-ui", "sans-serif"],
      },
      boxShadow: {
        panel: "0 0 0 1px #223040, 0 8px 24px -12px rgba(0,0,0,0.6)",
      },
      animation: {
        blink: "blink 1.6s step-start infinite",
      },
      keyframes: {
        blink: {
          "50%": { opacity: "0.25" },
        },
      },
    },
  },
  plugins: [],
};
