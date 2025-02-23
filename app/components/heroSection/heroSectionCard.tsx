import React from "react";
import Image from "next/image";

const HeroSectionCard: React.FC<{ url: string; isActive: boolean }> = (
  props
) => {
  return (
    <div
      className={`w-24 h-16 overflow-hidden rounded-lg cursor-pointer border-2 ${
        props.isActive ? "border-white" : "border-transparent"
      }`}
    >
      <Image
        src={props.url}
        alt="movie"
        width={96}
        height={64}
        className="object-cover w-full h-full"
      />
    </div>
  );
};

export default HeroSectionCard;
