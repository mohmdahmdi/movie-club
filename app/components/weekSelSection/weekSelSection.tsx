import domain from "@/app/assets/config/domain";
import useAxios from "@/app/hooks/useAxios";
import { useEffect } from "react";
import WeekCard from "./weekCard";

const WeekSelSection = () => {
  const { data, error, loading, get } = useAxios<[]>();

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
  return (
    <div className="mt-3 py-1 px-5">
      <div>
        <div className="mb-3">
          <span>{}</span> {/* Icon */}
          <span className="pr-2 text-xl font-bold">داغ ترین ها</span>
        </div>
      </div>
      <div className="grid grid-cols-8 width-full mx-2">
        {data?.map((element, index) => {
          return <WeekCard key={index} movie={element} />;
        })}
      </div>
    </div>
  );
}
 
export default WeekSelSection;