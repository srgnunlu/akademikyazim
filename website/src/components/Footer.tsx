import { useTranslations } from "next-intl";

export default function Footer() {
  const t = useTranslations("footer");

  return (
    <footer className="border-t border-border py-16 px-6">
      <div className="max-w-5xl mx-auto">
        <div className="grid sm:grid-cols-4 gap-10 mb-12">
          <div className="sm:col-span-1">
            <div className="text-sm font-bold mb-2">TezAtlas</div>
            <p className="text-xs text-muted leading-relaxed">
              {t("tagline")}
            </p>
          </div>

          <div>
            <div className="text-xs font-bold mb-3">{t("product")}</div>
            <div className="space-y-2">
              <a
                href="#features"
                className="block text-xs text-muted hover:text-foreground transition-colors"
              >
                {t("docs")}
              </a>
              <a
                href="#how-it-works"
                className="block text-xs text-muted hover:text-foreground transition-colors"
              >
                {t("quickStart")}
              </a>
            </div>
          </div>

          <div>
            <div className="text-xs font-bold mb-3">{t("resources")}</div>
            <div className="space-y-2">
              <a
                href="https://github.com/baristiran/tezatlas/blob/main/CONTRIBUTING.md"
                target="_blank"
                rel="noopener noreferrer"
                className="block text-xs text-muted hover:text-foreground transition-colors"
              >
                {t("contributing")}
              </a>
              <a
                href="https://github.com/baristiran/tezatlas/blob/main/LICENSE"
                target="_blank"
                rel="noopener noreferrer"
                className="block text-xs text-muted hover:text-foreground transition-colors"
              >
                {t("license")}
              </a>
            </div>
          </div>

          <div>
            <div className="text-xs font-bold mb-3">{t("community")}</div>
            <div className="space-y-2">
              <a
                href="https://github.com/baristiran/tezatlas"
                target="_blank"
                rel="noopener noreferrer"
                className="block text-xs text-muted hover:text-foreground transition-colors"
              >
                {t("github")}
              </a>
              <a
                href="https://github.com/baristiran/tezatlas/issues"
                target="_blank"
                rel="noopener noreferrer"
                className="block text-xs text-muted hover:text-foreground transition-colors"
              >
                {t("issues")}
              </a>
              <a
                href="https://github.com/baristiran/tezatlas/discussions"
                target="_blank"
                rel="noopener noreferrer"
                className="block text-xs text-muted hover:text-foreground transition-colors"
              >
                {t("discussions")}
              </a>
            </div>
          </div>
        </div>

        <div className="border-t border-border pt-6">
          <p className="text-xs text-muted">{t("copyright")}</p>
        </div>
      </div>
    </footer>
  );
}
