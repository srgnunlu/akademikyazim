import { useTranslations } from "next-intl";
import { Scale, Stethoscope, Cpu, Users, BookMarked } from "lucide-react";

export default function Disciplines() {
  const t = useTranslations("disciplines");

  const items = [
    { icon: Scale, key: "law" },
    { icon: Stethoscope, key: "medicine" },
    { icon: Cpu, key: "stem" },
    { icon: Users, key: "social" },
    { icon: BookMarked, key: "humanities" },
  ] as const;

  return (
    <section className="py-24 sm:py-32 px-6 bg-surface-alt">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {items.map((d) => (
            <div
              key={d.key}
              className="border border-border bg-surface p-6 hover:border-foreground/20 transition-colors"
            >
              <d.icon size={18} className="text-muted mb-3" />
              <h3 className="text-sm font-bold mb-2">{t(d.key)}</h3>
              <p className="text-xs text-muted leading-relaxed">
                {t(`${d.key}Desc`)}
              </p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
