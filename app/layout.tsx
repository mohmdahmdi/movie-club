import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Navbar from './components/navbar/navbar';

const vazir = localFont({
  src: "./assets/fonts/vazir/Vazir.woff",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "movie club",
  description:
    "A community for movie lovers",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${vazir.className} antialiased`}
      >
        <Navbar />
        {children}
      </body>
    </html>
  );
}
