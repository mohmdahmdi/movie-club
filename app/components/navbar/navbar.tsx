"use client";
import useNavScroll from "@/app/hooks/useNavScroll";

const Navbar = () => {
  const isScrolled = useNavScroll();
  return (
    <nav
      className={`w-full fixed top-0 flex text-center justify-center items-center py-2 gap-x-4 transition-colors ${
        isScrolled ? "bg-opacity-50 bg-neutral-700" : ""
      }`}
    >
      <h1 className="text-xl font-bold">تایتل سایت</h1>
      <div className="border rounded-full px-3 py-2">ورود / ثبت نام</div>
      <div>فیلم ها</div>
      <div>لیست ها</div>
      <div>اعضا</div>
      <div>ژورنال</div>
      <input
        className="border rounded-full py-1 px-2 text-sm"
        type="text"
        placeholder="جست و جو ..."
      />
    </nav>
  );
};

export default Navbar;
