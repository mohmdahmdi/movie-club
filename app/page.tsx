import HeroSection from "./components/heroSection/heroSection";
import HottestSection from './components/hottestSection/hottestSection';
export default function Home() {
  return (
    <div className="h-[200vh]">
      <HeroSection />
      <HottestSection />
    </div>
  );
}
