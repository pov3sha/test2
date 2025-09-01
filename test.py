import { useState } from "react";
import { motion } from "framer-motion";

export default function App() {
  const [page, setPage] = useState("home");
  const articles = [
    { id: 1, title: "The Future of AI in Everyday Life", excerpt: "How AI is shaping our world…", content: "Full article..." },
    { id: 2, title: "Top 10 Programming Languages in 2025", excerpt: "A breakdown of popular coding languages…", content: "Full article..." },
    { id: 3, title: "5G, 6G, and the Future of Connectivity", excerpt: "How ultra-fast internet transforms life…", content: "Full article..." },
  ];

  const renderPage = () => {
    switch (page) {
      case "home":
        return (
          <>
            {/* Hero Section */}
            <section className="relative h-[60vh] bg-gradient-to-br from-blue-900 to-purple-900 flex items-center justify-center text-center overflow-hidden">
              <motion.h1
                className="text-5xl md:text-6xl font-extrabold bg-clip-text text-transparent bg-gradient-to-r from-purple-400 to-blue-400"
                initial={{ y: 50, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
              >
                TechSphere Blog: Explore the Future
              </motion.h1>
              <motion.button
                onClick={() => setPage("articles")}
                className="mt-8 px-8 py-4 bg-purple-600 hover:bg-purple-700 rounded-lg text-white font-semibold"
                initial={{ scale: 0.8, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                transition={{ delay: 0.3 }}
              >
                Explore Articles
              </motion.button>
            </section>

            {/* Featured Carousel */}
            <section className="py-16 bg-gray-950">
              <h2 className="text-3xl font-bold text-center text-white mb-8">Featured Reads</h2>
              <div className="flex overflow-x-auto space-x-6 px-8">
                {articles.map(article => (
                  <motion.div
                    key={article.id}
                    className="min-w-[300px] bg-gray-800 rounded-2xl p-6 hover:shadow-2xl cursor-pointer"
                    whileHover={{ scale: 1.05 }}
                    onClick={() => setPage(`article-${article.id}`)}
                  >
                    <h3 className="text-xl font-semibold text-white">{article.title}</h3>
                    <p className="text-gray-400 mt-2">{article.excerpt}</p>
                  </motion.div>
                ))}
              </div>
            </section>

            {/* About Section with Background */}
            <section className="relative py-20 text-center text-white">
              <div className="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1950&q=80')] bg-cover bg-center opacity-30"></div>
              <motion.div
                className="relative max-w-3xl mx-auto space-y-6"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 0.5 }}
              >
                <h2 className="text-4xl font-bold">About TechSphere</h2>
                <p className="text-lg">
                  At TechSphere, we dissect AI, programming, and tech innovation—delivering insights with clarity and curiosity.
                </p>
              </motion.div>
            </section>
          </>
        );

      case "articles":
        return (
          <motion.div className="p-8" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
            <h1 className="text-3xl font-bold text-white mb-8">All Articles</h1>
            <div className="grid md:grid-cols-2 gap-8">
              {articles.map(a => (
                <motion.div
                  key={a.id}
                  className="bg-gray-800 p-6 rounded-xl cursor-pointer hover:bg-gray-700"
                  whileHover={{ x: 5 }}
                  onClick={() => setPage(`article-${a.id}`)}
                >
                  <h2 className="text-2xl text-purple-400">{a.title}</h2>
                  <p className="text-gray-400 mt-2">{a.excerpt}</p>
                </motion.div>
              ))}
            </div>
          </motion.div>
        );

      case "about":
        return (
          <motion.div className="p-8 max-w-3xl mx-auto text-center text-white" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
            <h1 className="text-3xl font-bold mb-4">About TechSphere</h1>
            <p>We’re passionate writers and tech lovers. We distill complex topics into insights that educate and inspire.</p>
          </motion.div>
        );

      case "contact":
        return (
          <motion.div className="p-8 max-w-xl mx-auto text-white" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
            <h1 className="text-3xl font-bold text-center mb-6">Contact Us</h1>
            <form className="space-y-4">
              <input type="text" placeholder="Your Name" className="w-full p-3 rounded-lg bg-gray-800" />
              <input type="email" placeholder="Your Email" className="w-full p-3 rounded-lg bg-gray-800" />
              <textarea placeholder="Your Message" className="w-full p-3 rounded-lg bg-gray-800"></textarea>
              <button className="w-full bg-purple-600 py-3 rounded-lg hover:bg-purple-700 text-white">
                Send Message
              </button>
            </form>
          </motion.div>
        );

      default:
        if (page.startsWith("article-")) {
          const id = parseInt(page.split("-")[1]);
          const art = articles.find(a => a.id === id);
          return (
            <motion.div className="p-8 max-w-3xl mx-auto text-white" initial={{ opacity: 0 }} animate={{ opacity: 1 }}>
              <h1 className="text-4xl font-bold mb-4">{art.title}</h1>
              <p className="text-gray-400">{art.content}</p>
              <button
                onClick={() => setPage("articles")}
                className="mt-6 px-4 py-2 bg-gray-700 rounded-lg hover:bg-gray-600"
              >
                Back to Articles
              </button>
            </motion.div>
          );
        }
        break;
    }
  };

  return (
    <div className="min-h-screen bg-gray-950 flex flex-col text-gray-200">
      <nav className="flex justify-between items-center p-6 bg-gray-900 shadow-lg">
        <h1 className="text-2xl font-bold text-purple-400 cursor-pointer" onClick={() => setPage("home")}>TechSphere</h1>
        <div className="space-x-6">
          {["home", "articles", "about", "contact"].map(p => (
            <button key={p} onClick={() => setPage(p)} className="hover:text-purple-400 uppercase">{p}</button>
          ))}
        </div>
      </nav>
      <main className="flex-grow">{renderPage()}</main>
      <footer className="bg-gray-900 text-center p-4 text-gray-500">© 2025 TechSphere Blog. All rights reserved.</footer>
    </div>
  );
}
