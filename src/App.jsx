import React, { useState } from 'react';
import './index.css';
import { weeklySummary } from './data.js';

const emptyCodeMessage =
  '# 코드모음집.py에서 이 문제와 연결되는 코드 섹션을 찾지 못했습니다.';

const ProblemCard = ({ problem }) => {
  const [showCode, setShowCode] = useState(false);
  const [showContribution, setShowContribution] = useState(false);
  const [showAdvanced, setShowAdvanced] = useState(false);
  const codeText = problem.code?.trim() ? problem.code : emptyCodeMessage;

  return (
    <div className="problem-card">
      <div className="problem-header">
        <div>
          <h3 className="problem-title">{problem.title}</h3>
          {problem.highlight && (
            <button
              className={`highlight-badge ${showAdvanced ? 'active' : ''}`}
              onClick={() => setShowAdvanced(!showAdvanced)}
              type="button"
            >
              {showAdvanced ? '심화 학습 닫기' : problem.highlight}
            </button>
          )}
        </div>
        <span className={`status-badge ${problem.completed ? 'completed' : 'pending'}`}>
          {problem.completed ? 'Completed' : 'In Progress'}
        </span>
      </div>

      {showAdvanced && (
        <div className="advanced-panel">
          <p>{problem.advancedLearning || problem.contribution}</p>
        </div>
      )}

      <div className="contribution-section">
        <button
          className="toggle-row"
          onClick={() => setShowContribution(!showContribution)}
          type="button"
        >
          <span>Contribution Details</span>
          <span>{showContribution ? '접기' : '펼치기'}</span>
        </button>

        {showContribution && <p className="contribution-desc">{problem.contribution}</p>}

        <div className="progress-container">
          <div className="progress-bar-bg">
            <div className="progress-bar-fill" style={{ width: `${problem.percentage}%` }} />
          </div>
          <span className="progress-text">{problem.percentage}%</span>
        </div>

        <div className="code-section">
          <button className="code-toggle" onClick={() => setShowCode(!showCode)} type="button">
            {showCode ? '코드 접기' : '코드 펼치기'}
          </button>

          {showCode && (
            <div className="code-panel">
              <div className="code-panel-header">
                <span>{problem.title}</span>
                <span>Python</span>
              </div>
              <pre className="code-block">
                <code>{codeText}</code>
              </pre>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

const WeekCard = ({ week }) => {
  return (
    <section className="week-section">
      <div className="week-header">
        <p className="week-label">{week.week}</p>
        <h2>{week.title}</h2>
        <p>{week.concept}</p>
      </div>
      <div className="problems-grid">
        {week.problems.map((problem) => (
          <ProblemCard key={problem.id} problem={problem} />
        ))}
      </div>
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
          All Weeks
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
        기여도는 구현, 검토, 발표 준비, 반례 점검, 제출 형식 확인 기록을 기준으로 표시했습니다. 확인되지 않은 단순 검토 항목은 15%로 표시했습니다.
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
  const displayData =
    activeWeek === 'All' ? weeklySummary : weeklySummary.filter((week) => week.week === activeWeek);

  const weekNumbers = weeklySummary.map((d) => d.week);

  return (
    <div className="dashboard-container">
      <Sidebar weeks={weekNumbers} activeWeek={activeWeek} setActiveWeek={setActiveWeek} />

      <main className="main-content">
        {activeWeek === 'All' && <TopSummary data={weeklySummary} />}

        {displayData.map((week) => (
          <WeekCard key={week.week} week={week} />
        ))}
      </main>
    </div>
  );
};

export default App;
