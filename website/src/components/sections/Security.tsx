import { useTranslations } from "next-intl";
import { Shield, HardDrive, Lock, Eye } from "lucide-react";

export default function Security() {
  const t = useTranslations("security");

  const items = [
    { icon: HardDrive, title: t("localTitle"), desc: t("localDesc") },
    { icon: Lock, title: t("noCloudTitle"), desc: t("noCloudDesc") },
    { icon: Eye, title: t("auditTitle"), desc: t("auditDesc") },
    { icon: Shield, title: t("gitTitle"), desc: t("gitDesc") },
  ];

  return (
    <section className="py-24 sm:py-32 px-6">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-3">
          {t("title")}
        </h2>
        <p className="text-muted text-base max-w-2xl mb-14">{t("subtitle")}</p>

        <div className="grid sm:grid-cols-2 gap-6">
          {items.map((s, i) => (
            <div
              key={i}
              className="border border-border bg-surface p-6 hover:border-foreground/20 transition-colors"
            >
              <s.icon size={18} className="text-muted mb-3" />
              <h3 className="text-sm font-bold mb-2">{s.title}</h3>
              <p className="text-xs text-muted leading-relaxed">{s.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
