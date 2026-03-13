import type { MetadataRoute } from "next";

const BASE_URL = "https://tezatlas.com";

export default function sitemap(): MetadataRoute.Sitemap {
  const lastModified = new Date();

  return [
    {
      url: `${BASE_URL}/tr`,
      lastModified,
      changeFrequency: "weekly",
      priority: 1,
      alternates: {
        languages: { tr: `${BASE_URL}/tr`, en: `${BASE_URL}/en` },
      },
    },
    {
      url: `${BASE_URL}/en`,
      lastModified,
      changeFrequency: "weekly",
      priority: 0.9,
      alternates: {
        languages: { tr: `${BASE_URL}/tr`, en: `${BASE_URL}/en` },
      },
    },
  ];
}
