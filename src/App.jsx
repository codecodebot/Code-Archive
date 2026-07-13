import React, { useState } from 'react';
import './index.css';
import { dummyData, weeklySummary } from './data.js';

const ProblemCard = ({ problem }) => {
  const [showCode, setShowCode] = useState(false);
  const [showContribution, setShowContribution] = useState(false);

  return (
    <div className="problem-card">
      <div className="problem-header">
        <h3 className="problem-title">{problem.title}</h3>
        <span className={`status-badge ${problem.completed ? 'completed' : 'pending'}`}>
          {problem.completed ? 'Completed' : 'In Progress'}
        </span>
      </div>

      <div className="contribution-section">
        <div
          style={{
            display: 'flex',
            justifyContent: 'space-between',
            alignItems: 'center',
            cursor: 'pointer',
            marginBottom: '0.5rem',
          }}
          onClick={() => setShowContribution(!showContribution)}
        >
          <h4 style={{ margin: 0 }}>Contribution Details</h4>
          <span style={{ fontSize: '0.8rem', color: '#2b5c8f' }}>
            {showContribution ? '접기' : '펴기'}
          </span>
        </div>

        {showContribution && (
          <p className="contribution-desc" style={{ marginTop: '0.5rem' }}>
            {problem.contribution}
          </p>
        )}

        <div className="progress-container" style={{ marginTop: showContribution ? '1rem' : '0.5rem' }}>
          <div className="progress-bar-bg">
            <div className="progress-bar-fill" style={{ width: `${problem.percentage}%` }} />
          </div>
          <span className="progress-text">{problem.percentage}%</span>
        </div>

        {problem.code && (
          <div style={{ marginTop: '1.5rem', paddingTop: '1rem', borderTop: '1px solid #e9ecef' }}>
            <button
              onClick={() => setShowCode(!showCode)}
              style={{
                background: 'none',
                border: '1px solid #2b5c8f',
                color: '#2b5c8f',
                padding: '0.4rem 0.8rem',
                borderRadius: '4px',
                cursor: 'pointer',
                fontWeight: '500',
                fontSize: '0.875rem',
                transition: 'all 0.2s',
                width: '100%',
              }}
            >
              {showCode ? 'Hide Code' : 'View Code'}
            </button>

            {showCode && (
              <pre
                style={{
                  background: '#282c34',
                  color: '#abb2bf',
                  padding: '1rem',
                  borderRadius: '6px',
                  overflowX: 'auto',
                  fontSize: '0.85rem',
                  marginTop: '1rem',
                  maxHeight: '300px',
                }}
              >
                <code>{problem.code}</code>
              </pre>
            )}
          </div>
        )}
      </div>
    </div>
  );
};

const ProblemSection = ({ item }) => {
  return (
    <section className="week-section problem-section">
      <div className="week-header">
        <p className="week-label">{item.week}</p>
        <h2>{item.weekTitle}</h2>
        <p>{item.weekConcept}</p>
      </div>
      <ProblemCard problem={item} />
    </section>
  );
};

const Sidebar = ({ weeks, activeWeek, setActiveWeek }) => {
  return (
    <aside className="sidebar">
      <h2>Archive Menu</h2>
      <ul className="nav-list">
        <li
          className={`nav-item ${activeWeek === 'All' ? 'active' : ''}`}
          onClick={() => setActiveWeek('All')}
        >
          All Problems
        </li>
        {weeks.map((w) => (
          <li
            key={w}
            className={`nav-item ${activeWeek === w ? 'active' : ''}`}
            onClick={() => setActiveWeek(w)}
          >
            {w}
          </li>
        ))}
      </ul>
    </aside>
  );
};

const TopSummary = ({ data }) => {
  const totalWeeks = data.length;
  const totalProblems = data.reduce((acc, week) => acc + week.problems.length, 0);
  const completedProblems = data.reduce((acc, week) => acc + week.problems.filter((p) => p.completed).length, 0);

  const totalPercentage = data.reduce((acc, week) => {
    return acc + week.problems.reduce((sum, p) => sum + p.percentage, 0);
  }, 0);

  const avgContribution = totalProblems ? Math.round(totalPercentage / totalProblems) : 0;

  return (
    <div className="top-summary">
      <div className="summary-note">
        기여도는 확인된 구현·검수·발표 준비 기록을 기준으로 표시하고, 확인되지 않은 항목만 검토 30%로 표시합니다.
      </div>
      <div className="summary-card">
        <h3>Total Weeks</h3>
        <p className="value">{totalWeeks}</p>
      </div>
      <div className="summary-card">
        <h3>Problems Completed</h3>
        <p className="value">
          {completedProblems} / {totalProblems}
        </p>
      </div>
      <div className="summary-card">
        <h3>Average Contribution</h3>
        <p className="value">{avgContribution}%</p>
      </div>
    </div>
  );
};

const App = () => {
  const [activeWeek, setActiveWeek] = useState('All');
  // Force a refresh of the Vite dev client so the browser picks up the latest data.

  const displayData =
    activeWeek === 'All' ? dummyData : dummyData.filter((item) => item.week === activeWeek);

  const weekNumbers = weeklySummary.map((d) => d.week);

  return (
    <div className="dashboard-container">
      <Sidebar weeks={weekNumbers} activeWeek={activeWeek} setActiveWeek={setActiveWeek} />

      <main className="main-content">
        {activeWeek === 'All' && <TopSummary data={weeklySummary} />}

        {displayData.map((item) => (
          <ProblemSection key={item.id} item={item} />
        ))}
      </main>
    </div>
  );
};

export default App;
