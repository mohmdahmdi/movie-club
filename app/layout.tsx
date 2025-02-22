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
        <nav className="w-full fixed top-0 flex text-center justify-center items-center py-2 gap-x-3">
          <h1 className="text-xl font-bold">تایتل سایت</h1>
          <div className="border rounded-full px-3 py-2">ورود / ثبت نام</div>
          <div>فیلم ها</div>
          <div>لیست ها</div>
          <div>اعضا</div>
          <div>ژورنال</div>
          <input className="border rounded-full p-1" type="text" placeholder="جست و جو ..." />
        </nav>
        {children}
      </body>
    </html>
  );
}
