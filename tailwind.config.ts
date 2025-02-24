import type { Config } from "tailwindcss";

export default {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        'yellow-1': "rgba(var(--yellow1))",
        'yellow-2': "rgba(var(--yellow2))",
        'yellow-3': "rgba(var(--yellow3))",
        'gray-1': "rgba(var(--gray1))",
        'gray-2': "rgba(var(--gray2))",
        'gray-3': "rgba(var(--gray3))",
        blue : "rgba(var(--blue))"
      },
    },
  },
  plugins: [],
} satisfies Config;
