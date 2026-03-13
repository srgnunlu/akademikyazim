import { useTranslations } from "next-intl";
import { Terminal, Rocket, PenTool } from "lucide-react";

export default function HowItWorks() {
  const t = useTranslations("howItWorks");

  const steps = [
    {
      icon: Terminal,
      num: "01",
      title: t("step1title"),
      code: t("step1"),
    },
    {
      icon: Rocket,
      num: "02",
      title: t("step2title"),
      code: t("step2"),
    },
    {
      icon: PenTool,
      num: "03",
      title: t("step3title"),
      code: t("step3"),
    },
  ];

  return (
    <section id="how-it-works" className="py-24 sm:py-32 px-6">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div className="grid md:grid-cols-3 gap-8 mb-12">
          {steps.map((s) => (
            <div key={s.num}>
              <div className="flex items-center gap-3 mb-4">
                <span className="text-xs text-muted font-mono">{s.num}</span>
                <s.icon size={18} className="text-foreground" />
                <span className="text-sm font-bold">{s.title}</span>
              </div>
              <div className="bg-foreground text-background px-4 py-3 text-xs font-mono leading-relaxed">
                {s.code}
              </div>
            </div>
          ))}
        </div>

        <p className="text-sm text-muted leading-relaxed max-w-3xl">
          {t("detail")}
        </p>
      </div>
    </section>
  );
}
