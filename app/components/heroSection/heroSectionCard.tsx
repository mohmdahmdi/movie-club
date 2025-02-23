import React from "react";
import Image from "next/image";

const HeroSectionCard: React.FC<{ url: string; isActive: boolean }> = (
  props
) => {
  return (
    <div
      className={`overflow-hidden rounded-lg cursor-pointer transition-all -translate-y-4 ${
        props.isActive ? "border w-28 h-40 -translate-y-11 duration-500" : "w-24 h-32"
      }`}
    >
      <Image
        src={props.url}
        alt="movie"
        width={96}
        height={192}
        className="object-cover w-full h-full"
      />
    </div>
  );
};

export default HeroSectionCard;
