export const getNews = async (num, options) => {
  const url = `http://localhost:5000/get_news/${num}`;
  const response = await fetch(url, options)
  const news = response.json()
  return news
}

export const getCategory = async (num, options) => {
  const url = `http://localhost:5000/category/${num}`;
  const response = await fetch(url, options)
  const news = response.json()
  return news
}

export const getFiveCategory = async (options) => {
  const url = `http://localhost:5000/endpoint`;
  const response = await fetch(url, options)
  const news = response.json()
  return news
}

