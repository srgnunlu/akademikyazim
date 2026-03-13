import { useTranslations } from "next-intl";
import { Github, BookOpen } from "lucide-react";
import Image from "next/image";

export default function Hero() {
  const t = useTranslations("hero");

  return (
    <section className="relative min-h-screen flex items-center justify-center overflow-hidden">
      <Image
        src="/hero-bg.jpeg"
        alt=""
        fill
        priority
        className="object-cover"
      />
      <div className="absolute inset-0 bg-black/50" />

      <div className="relative z-10 max-w-4xl mx-auto px-6 text-center">
        <p className="text-xs tracking-[0.3em] uppercase text-white/60 mb-6 animate-fade-in font-mono">
          {t("tagline")}
        </p>
        <h1 className="text-4xl sm:text-5xl md:text-6xl lg:text-7xl font-bold text-white tracking-tight leading-[1.1] mb-6 animate-fade-in-delay-1">
          {t("headline")}
        </h1>
        <p className="text-sm sm:text-base text-white/70 tracking-widest mb-10 animate-fade-in-delay-2 font-mono">
          {t("sub")}
        </p>
        <div className="flex flex-col sm:flex-row items-center justify-center gap-4 animate-fade-in-delay-3">
          <a
            href="https://github.com/baristiran/tezatlas"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 bg-white text-black px-6 py-3 text-sm font-medium hover:bg-white/90 transition-colors"
          >
            <Github size={16} />
            {t("cta")}
          </a>
          <a
            href="https://github.com/baristiran/tezatlas#1-what-is-tezatlas"
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 border border-white/30 text-white px-6 py-3 text-sm font-medium hover:bg-white/10 transition-colors"
          >
            <BookOpen size={16} />
            {t("ctaSecondary")}
          </a>
        </div>
      </div>

      <div className="absolute bottom-8 left-1/2 -translate-x-1/2 animate-bounce">
        <div className="w-px h-8 bg-white/30" />
      </div>
    </section>
  );
}
