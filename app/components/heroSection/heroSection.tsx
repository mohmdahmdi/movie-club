"use client";

import domain from "@/app/assets/config/domain";
import useAxios from "@/app/hooks/useAxios";
import { useEffect, useState } from "react";
import { ISliderGetResponse } from "../../assets/interfaces/endpoints";
import Image from "next/image";
import HeroSectionCard from "./heroSectionCard";

const HeroSection = () => {
  const { data, error, loading, get } = useAxios<ISliderGetResponse[]>();
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    get(domain + "/api/slider");
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    if (data && data.length > 0) {
      const interval = setInterval(() => {
        setCurrentIndex((prevIndex) => (prevIndex + 1) % data.length);
      }, 5000);

      return () => clearInterval(interval);
    }
  }, [data]);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  if (!data || data.length === 0) return <div>No images found</div>;

  return (
    <div className="relative w-full h-[100vh] -z-10 brightness-[70%]">
      <Image
        src={data[currentIndex].url}
        alt={data[currentIndex].title}
        fill
        className="object-cover"
        priority
      />

      <div className="absolute inset-0 bg-gradient-to-t from-black/100 to-transparent w-full h-full"></div>

      <div className="absolute bottom-2 left-1/2 transform -translate-x-1/2 flex gap-4 bg-[rgba(18, 18, 18, 0.9)] rounded-t-3xl  px-10">
        {data.map((element, index) => (
          <HeroSectionCard
            key={index}
            url={element.poster}
            isActive={index === currentIndex}
          />
        ))}
      </div>
    </div>
  );
};

export default HeroSection;
