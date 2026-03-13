import type { Metadata } from "next";
import { Geist_Mono } from "next/font/google";
import { NextIntlClientProvider, hasLocale } from "next-intl";
import { getMessages, getTranslations } from "next-intl/server";
import { notFound } from "next/navigation";
import { routing } from "@/i18n/routing";
import "../globals.css";

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin", "latin-ext"],
  display: "swap",
  weight: ["400", "500", "600", "700"],
});

export async function generateMetadata({
  params,
}: {
  params: Promise<{ locale: string }>;
}): Promise<Metadata> {
  const { locale } = await params;
  const t = await getTranslations({ locale, namespace: "meta" });

  const baseUrl = "https://tezatlas.com";

  return {
    title: t("title"),
    description: t("description"),
    alternates: {
      canonical: `${baseUrl}/${locale}`,
      languages: {
        tr: `${baseUrl}/tr`,
        en: `${baseUrl}/en`,
      },
    },
    openGraph: {
      title: t("title"),
      description: t("description"),
      type: "website",
      url: `${baseUrl}/${locale}`,
      locale: locale === "tr" ? "tr_TR" : "en_US",
    },
    twitter: {
      card: "summary_large_image",
      title: t("title"),
      description: t("description"),
    },
  };
}

export default async function LocaleLayout({
  children,
  params,
}: {
  children: React.ReactNode;
  params: Promise<{ locale: string }>;
}) {
  const { locale } = await params;
  if (!hasLocale(routing.locales, locale)) {
    notFound();
  }

  const messages = await getMessages();

  return (
    <html lang={locale} dir="ltr">
      <body className={`${geistMono.variable} antialiased`}>
        <NextIntlClientProvider messages={messages}>
          {children}
        </NextIntlClientProvider>
      </body>
    </html>
  );
}
