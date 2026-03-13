import { useTranslations } from "next-intl";
import { MessageSquare, FileEdit } from "lucide-react";

export default function Modes() {
  const t = useTranslations("modes");

  return (
    <section className="py-24 sm:py-32 px-6 bg-surface-alt">
      <div className="max-w-5xl mx-auto">
        <span className="text-xs tracking-[0.2em] uppercase text-muted font-mono">
          {t("badge")}
        </span>
        <h2 className="text-3xl sm:text-4xl font-bold tracking-tight mt-3 mb-14">
          {t("title")}
        </h2>

        <div className="grid md:grid-cols-2 gap-8 mb-10">
          <div className="border border-border bg-surface p-8">
            <div className="flex items-center gap-3 mb-1">
              <MessageSquare size={18} />
              <h3 className="text-base font-bold">{t("mode1title")}</h3>
            </div>
            <span className="text-xs text-muted font-mono mb-4 block">
              {t("mode1subtitle")}
            </span>
            <p className="text-sm text-muted italic mb-4">{t("mode1desc")}</p>
            <p className="text-sm text-muted leading-relaxed">
              {t("mode1detail")}
            </p>
          </div>

          <div className="border border-border bg-surface p-8">
            <div className="flex items-center gap-3 mb-1">
              <FileEdit size={18} />
              <h3 className="text-base font-bold">{t("mode2title")}</h3>
            </div>
            <span className="text-xs text-muted font-mono mb-4 block">
              {t("mode2subtitle")}
            </span>
            <p className="text-sm text-muted italic mb-4">{t("mode2desc")}</p>
            <p className="text-sm text-muted leading-relaxed">
              {t("mode2detail")}
            </p>
          </div>
        </div>

        <div className="border-l-2 border-foreground pl-6">
          <p className="text-sm font-medium">{t("hardRule")}</p>
        </div>
      </div>
    </section>
  );
}
