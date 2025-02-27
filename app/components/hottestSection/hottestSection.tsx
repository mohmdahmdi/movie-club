"use client";

import domain from "@/app/assets/config/domain";
import { ISliderGetResponse } from "@/app/assets/interfaces/endpoints";
import useAxios from "@/app/hooks/useAxios";
import LocalFireDepartmentIcon from "@mui/icons-material/LocalFireDepartment";
import { useEffect } from "react";
import HotCard from "./hotCard";

const HottestSection = () => {
  const { data, error, loading, get } = useAxios<ISliderGetResponse[]>();

  useEffect(() => {
    get(domain + "/api/movie/hottest");
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  if (loading && !data) {
    return (
      <div>
        <span>Loading...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div>
        <span>Error: {error.message}</span>
      </div>
    );
  }

  return (
    <div className="mt-3 py-1 px-5">
      <div>
        <div className="mb-3">
          <span>{<LocalFireDepartmentIcon />}</span>
          <span className="pr-2 text-xl font-bold">داغ ترین ها</span>
        </div>
      </div>
      <div className="grid grid-cols-8 width-full mx-2">
        {data?.map((element, index) => {
          return <HotCard key={index} movie={element} />;
        })}
      </div>
    </div>
  );
};

export default HottestSection;
