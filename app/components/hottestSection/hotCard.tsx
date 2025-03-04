import { ISliderGetResponse } from "@/app/assets/interfaces/endpoints";
import Image from "next/image";
import Link from "next/link";

const HotCard: React.FC<{ movie: ISliderGetResponse }> = (props) => {
  return (
    <Link href={`/movie/${props.movie.movie_id}`} className="col-span-1 bg-gray-1 mx-2 px-2 rounded-lg hover:bg-gray-2 transition-all ease-linear duration-200 cursor-pointer">
      <div className="items-center place-self-center pt-2 mb-4">
        <Image
          src={props.movie.poster}
          alt={`فیلم ${props.movie.title}`}
          width={150}
          height={300}
          className="h-[230px] rounded-lg"
        />
      </div>
      <div className="text-center ltr">
        <div className="text-ellipss break-words line-clamp-1 ltr hover:text-blue transition-colors ease-linear duration-200 cursor-pointer">
          {props.movie.title}
        </div>
        <div>{props.movie.year}</div>
      </div>
    </Link>
  );
};

export default HotCard;
