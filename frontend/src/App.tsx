function App() {
  return (
    <main className="page-shell">
      <header className="topbar">
        <a className="brand" href="/" aria-label="Resume AI Analyzer home">
          <span className="brand-mark" aria-hidden="true">
            R
          </span>
          <span>Resume AI Analyzer</span>
        </a>
        <span className="topbar-note">A clearer next step</span>
      </header>

      <section className="intro" aria-labelledby="page-title">
        <p className="eyebrow">
          <span className="eyebrow-dot" /> YOUR CAREER, IN FOCUS
        </p>
        <h1 id="page-title">
          Make your next move
          <br />
          with <em>confidence.</em>
        </h1>
        <p className="intro-copy">
          Get ready to put your experience into words. A thoughtful resume
          review is on its way.
        </p>
      </section>

      <section className="upload-section" aria-labelledby="upload-title">
        <div className="section-heading">
          <div>
            <p className="step-label">
              01 <span /> GET STARTED
            </p>
            <h2 id="upload-title">Your resume, when you’re ready.</h2>
          </div>
          <span className="coming-soon">COMING SOON</span>
        </div>
        <div className="upload-placeholder" aria-disabled="true">
          <span className="upload-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none">
              <path d="M12 15V4m0 0L8 8m4-4 4 4M5 14v5h14v-5" />
            </svg>
          </span>
          <p className="upload-title">Upload your resume</p>
          <p className="upload-hint">
            PDF or DOCX · Upload will be enabled in a future update
          </p>
        </div>
        <p className="privacy-note">
          <span aria-hidden="true">◇</span> Your documents will stay yours.
          Privacy is part of the plan.
        </p>
      </section>

      <footer className="footer">
        <span>Built for the work you want next.</span>
        <span className="footer-mark">
          RA<span>.</span>
        </span>
      </footer>
    </main>
  );
}

export default App;
