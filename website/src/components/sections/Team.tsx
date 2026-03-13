import { useTranslations } from "next-intl";

export default function Team() {
  const t = useTranslations("team");

  return (
    <section className="py-24 sm:py-32 px-6 bg-surface-alt">
      <div className="max-w-3xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div className="space-y-8">
          <div>
            <div className="text-xs text-muted font-mono mb-1">
              {t("architect")}
            </div>
            <div className="text-lg font-bold">{t("architectName")}</div>
          </div>

          <div className="border-t border-border pt-8">
            <div className="text-xs text-muted font-mono mb-2">
              {t("mission")}
            </div>
            <p className="text-sm leading-relaxed">{t("missionText")}</p>
          </div>

          <div className="border-t border-border pt-8">
            <div className="text-xs text-muted font-mono mb-2">
              {t("vision")}
            </div>
            <p className="text-sm leading-relaxed">{t("visionText")}</p>
          </div>

          <div className="border-t border-border pt-8">
            <div className="text-xs text-muted font-mono mb-2">
              {t("nameOrigin")}
            </div>
            <p className="text-sm leading-relaxed">{t("nameOriginText")}</p>
          </div>

          <div className="border-t border-border pt-8">
            <p className="text-xs text-muted font-mono">{t("builtOn")}</p>
          </div>
        </div>
      </div>
    </section>
  );
}
