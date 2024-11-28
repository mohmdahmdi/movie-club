import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const vazir = localFont({
  src: "./assets/fonts/vazir/Vazir.woff",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "book club",
  description:
    "An online community for book lovers",
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
        <nav>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
          <div></div>
        </nav>
        {children}
      </body>
    </html>
  );
}
