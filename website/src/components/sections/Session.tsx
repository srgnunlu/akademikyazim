import { useTranslations } from "next-intl";
import { RotateCcw, Flame, BarChart3 } from "lucide-react";

export default function Session() {
  const t = useTranslations("session");

  const items = [
    { icon: RotateCcw, title: t("srl"), desc: t("srlDesc") },
    { icon: Flame, title: t("streak"), desc: t("streakDesc") },
    { icon: BarChart3, title: t("dashboard"), desc: t("dashboardDesc") },
  ];

  return (
    <section className="py-24 sm:py-32 px-6">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div className="grid md:grid-cols-3 gap-6 mb-10">
          {items.map((s, i) => (
            <div key={i} className="border border-border bg-surface p-6">
              <s.icon size={18} className="text-muted mb-3" />
              <h3 className="text-sm font-bold mb-2">{s.title}</h3>
              <p className="text-xs text-muted leading-relaxed">{s.desc}</p>
            </div>
          ))}
        </div>

        <div className="bg-foreground text-background p-6 font-mono text-xs leading-loose">
          <div className="text-white/50 mb-1">/status</div>
          <div>
            → Phase: 3 (Systematic Reading) | Article | Economics
          </div>
          <div>→ Sources: 18 read / 34 total | Saturation: ~41%</div>
          <div>→ Last session: 2 days ago | Streak: 8 (best: 12)</div>
          <div>→ Next action: Read Jones (2020) — tagged high-priority</div>
          <div>→ Open blocker: Awaiting Smith (2019) PDF from ILL</div>
        </div>
      </div>
    </section>
  );
}
