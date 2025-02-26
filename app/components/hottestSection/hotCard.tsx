import { ISliderGetResponse } from "@/app/assets/interfaces/endpoints";
import Image from "next/image";

const HotCard: React.FC<{ movie: ISliderGetResponse }> = (props) => {
  return (
    <div className="col-span-1 bg-gray-1 mx-3">
      <div className="items-center place-self-center">
        <Image
          src={props.movie.poster}
          alt={`فیلم ${props.movie.title}`}
          width={100}
          height={300}
        />
      </div>
      <div className="text-center">
        <div>{props.movie.title}</div>
        <div>{props.movie.year}</div>
      </div>
    </div>
  );
};

export default HotCard;
