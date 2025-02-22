"use client";

import domain from "@/app/assets/config/domain";
import useAxios from "@/app/hooks/useAxios";
import { useEffect, useState } from "react";
import { ISliderGetResponse } from "../../assets/interfaces/endpoints";
import Image from "next/image";
import { relative } from "path";

const MainPhoto = () => {
  const { data, error, loading, get } = useAxios<ISliderGetResponse[]>();
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    get(domain + "/api/slider");
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
    <div className="relative w-[100%] h-[100vh] -z-10">
      <Image
        src={data[currentIndex].url}
        alt={data[currentIndex].title}
        fill
        style={{ objectFit: "cover" }}
        priority
      />
    </div>
  );
};

export default MainPhoto;
