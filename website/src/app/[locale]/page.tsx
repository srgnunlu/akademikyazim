import Navigation from "@/components/Navigation";
import Hero from "@/components/sections/Hero";
import Problem from "@/components/sections/Problem";
import Stats from "@/components/sections/Stats";
import Features from "@/components/sections/Features";
import HowItWorks from "@/components/sections/HowItWorks";
import Modes from "@/components/sections/Modes";
import DocTypes from "@/components/sections/DocTypes";
import IronRules from "@/components/sections/IronRules";
import TechStack from "@/components/sections/TechStack";
import Disciplines from "@/components/sections/Disciplines";
import Comparison from "@/components/sections/Comparison";
import Research from "@/components/sections/Research";
import Session from "@/components/sections/Session";
import Security from "@/components/sections/Security";
import Testimonials from "@/components/sections/Testimonials";
import Roadmap from "@/components/sections/Roadmap";
import FAQ from "@/components/sections/FAQ";
import Team from "@/components/sections/Team";
import CTA from "@/components/sections/CTA";
import Footer from "@/components/Footer";
import FAQJsonLd from "@/components/FAQJsonLd";

export default async function Home({
  params,
}: {
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;

  return (
    <>
      <FAQJsonLd locale={locale} />
      <Navigation />
      <main>
        <Hero />
        <Problem />
        <Stats />
        <Features />
        <HowItWorks />
        <Modes />
        <DocTypes />
        <IronRules />
        <TechStack />
        <Disciplines />
        <Comparison />
        <Research />
        <Session />
        <Security />
        <Testimonials />
        <Roadmap />
        <FAQ />
        <Team />
        <CTA />
      </main>
      <Footer />
    </>
  );
}
