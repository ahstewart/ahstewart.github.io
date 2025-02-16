Title: Resume
Author: Andrew Stewart
Summary: Resume

%% start of file `template.tex'.
%% Copyright 2006-2013 Xavier Danaux (xdanaux@gmail.com).
%
% This work may be distributed and/or modified under the
% conditions of the LaTeX Project Public License version 1.3c,
% available at http://www.latex-project.org/lppl/.


\documentclass[11pt,legalpaper,roman]{moderncv}        % possible options include font size ('10pt', '11pt' and '12pt'), paper size ('a4paper', 'letterpaper', 'a5paper', 'legalpaper', 'executivepaper' and 'landscape') and font family ('sans' and 'roman')

% modern themes
\moderncvstyle{banking}                            % style options are 'casual' (default), 'classic', 'oldstyle' and 'banking'
\moderncvcolor{blue}                                % color options 'blue' (default), 'orange', 'green', 'red', 'purple', 'grey' and 'black'
%\renewcommand{\familydefault}{\sfdefault}         % to set the default font; use '\sfdefault' for the default sans serif font, '\rmdefault' for the default roman one, or any tex font name
\nopagenumbers{}                                  % uncomment to suppress automatic page numbering for CVs longer than one page

% character encoding
\usepackage[utf8]{inputenc}
\usepackage{fontawesome}
\usepackage{tabularx}
\usepackage{ragged2e}
% if you are not using xelatex ou lualatex, replace by the encoding you are using
%\usepackage{CJKutf8}                              % if you need to use CJK to typeset your resume in Chinese, Japanese or Korean

% adjust the page margins
\usepackage[scale=.9]{geometry}
\usepackage{multicol}

\usepackage{listings}
\lstset{language=C,keywordstyle={\bfseries \color{blue}}}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    filecolor=magenta,      
    urlcolor=cyan,}

%\setlength{\hintscolumnwidth}{3cm}                % if you want to change the width of the column with the dates
%\setlength{\makecvtitlenamewidth}{10cm}           % for the 'classic' style, if you want to force the width allocated to your name and avoid line breaks. be careful though, the length is normally calculated to avoid any overlap with your personal info; use this at your own typographical risks...

\usepackage{import}

% personal data
\name{Andrew}{Stewart}
% \title{Curriculum Vitae}                               % optional, remove / comment the line if not wanted
\address{Redlands, CA}{}{}% optional, remove / comment the line if not wanted; the "postcode city" and and "country" arguments can be omitted or provided empty
% \phone[mobile]{909-839-3097}                   % optional, remove / comment the line if not wanted
% \phone[fixed]{01234 123456}                    % optional, remove / comment the line if not wanted
%\phone[fax]{+3~(456)~789~012}                      % optional, remove / comment the line if not wanted
% \email{xpan1@swarthmore.edu}                               % optional, remove / comment the line if not wanted
% \homepage{shawnpan.me}                         % optional, remove / comment the line if not wanted
% \extrainfo{}                 % optional, remove / comment the line if not wanted
%\photo[64pt][0.4pt]{picture}                       % optional, remove / comment the line if not wanted; '64pt' is the height the picture must be resized to, 0.4pt is the thickness of the frame around it (put it to 0pt for no frame) and 'picture' is the name of the picture file
%\quote{Some quote}                                 % optional, remove / comment the line if not wanted

% to show numerical labels in the bibliography (default is to show no labels); only useful if you make citations in your resume
%\makeatletter
%\renewcommand*{\bibliographyitemlabel}{\@biblabel{\arabic{enumiv}}}
%\makeatother
%\renewcommand*{\bibliographyitemlabel}{[\arabic{enumiv}]}% CONSIDER REPLACING THE ABOVE BY THIS

% bibliography with mutiple entries
%\usepackage{multibib}
%\newcites{book,misc}{{Books},{Others}}
  
\newcommand*{\customcventry}[7][.25em]{
  \begin{tabular}{@{}l} 
    {\bfseries #4}
  \end{tabular}
  \hfill% move it to the right
  \begin{tabular}{l@{}}
     {\bfseries #5}
  \end{tabular} \\
  \begin{tabular}{@{}l} 
    {\itshape #3}
  \end{tabular}
  \hfill% move it to the right
  \begin{tabular}{l@{}}
     {\itshape #2}
  \end{tabular}
  \ifx&#7&%
  \else{\\%
    \begin{minipage}{\maincolumnwidth}%
      \small#7%
    \end{minipage}}\fi%
  \par\addvspace{#1}}

\newcommand*{\customcvproject}[4][.25em]{
%   \vfill\noindent
  \begin{tabular}{@{}l} 
    {\bfseries #2}
  \end{tabular}
  \hfill% move it to the right
  \begin{tabular}{l@{}}
     {\itshape #3}
  \end{tabular}
  \ifx&#4&%
  \else{\\%
    \begin{minipage}{\maincolumnwidth}%
      \small#4%
    \end{minipage}}\fi%
  \par\addvspace{#1}}

\setlength{\tabcolsep}{12pt}

%----------------------------------------------------------------------------------
%            content
%----------------------------------------------------------------------------------
\begin{document}
\vspace*{-10.5mm}
%\begin{CJK*}{UTF8}{gbsn}                          % to typeset your resume in Chinese using CJK
%-----       resume       ---------------------------------------------------------
\makecvtitle
\vspace*{-24mm}

\begin{center}
\begin{tabular}{ c c c c }
 \faEnvelopeO\enspace ah.stewart@outlook.com & \faGithub\enspace \href{https://github.com/ahstewart}{ahstewart} &  \faMobile\enspace (951) 318-5180  
\end{tabular}
\end{center}

\section{EXPERIENCE}

{\customcventry{February 2024 - Present}{Product Manager - Analytics \& Reporting}{Cayuse LLC}{Redlands, CA (Remote)}{}
{\begin{itemize}
  \item Responsible for the development and launch of a new suite of data analytics and reporting products.  \vspace*{1mm}
  \item Launched first product (an analytics dashboard) in early 2024. The product has seen 15\% growth quarter over quarter since launch and will possess a positive contribution margin in its first year. 
  \vspace*{1mm}
{\end{itemize}
 }}
{\customcventry{October 2022 - Present}{Product Manager - Proposals S2S}{Cayuse LLC}{Redlands, CA (Remote)}{}
{\begin{itemize}
  \item Owns the development and maintenance of the Proposals S2S product strategy, roadmap, and backlog, working with both customers and internal stakeholders to make informed decisions.  \vspace*{1mm}
  \item Leads all team agile ceremonies and owns the product's release pipeline.  \vspace*{1mm}
  \item Since assuming the PM/PO role on the team:  \vspace*{1mm}
    \begin{itemize}
        \item Product has consistently boasted the highest NPS and ARR at the company.   \vspace*{1mm}
        \item Product software quality has increased quarter over quarter by an average of 9\%. (Quality here is an internal metric that is a function of support ticket rate, bug density, server downtime, and more).   \vspace*{1mm}
        \item Product vision and strategy has been redefined and evangelized, obtaining alignment throughout the organization.   \vspace*{1mm}
        \item Product team has spearheaded effort to build out integrations with multiple Cayuse products and external services.  \vspace*{1mm}
    \end{itemize}
  \end{itemize}
  \vspace*{1mm}
 }}
{\customcventry{November 2021 - October 2022}{Product Owner}{Cayuse LLC}{Redlands, CA (Remote)}{}
{\begin{itemize}
  \item As PO for Cayuse's flagship SaaS product, Sponsored Projects, coordinated with the Product Manager and other internal stakeholders to define product epics, create user stories, and plan releases.  \vspace*{1mm}
  \item Conducted weekly planning sessions to maintain and refine the team backlog.   \vspace*{1mm}
  \item Leveraged historical team data and various agile metrics to make intelligent decisions on backlog prioritization and PI/sprint planning.  \vspace*{1mm}
  \item Oversaw the release of several major features over a 6 month period that solidified the product's standing in APAC markets.  \vspace*{1mm}
  \end{itemize}
  \vspace*{1mm}
 }}
{\customcventry{May 2020 - November 2021}{Business Analyst}{iMedRIS Data Corporation}{Redlands, CA}{}
{\begin{itemize}
  \item Collaborated with Customer Success, Project Management, and Engineering teams to create feature requirement documentation and oversee feature development.  \vspace*{1mm}
  \item Acted as the company's Content Manager, which included overseeing the company's customer-facing Confluence site, writing and publishing technical manuals for more than 12 products, and developing release and patch notes.
  \end{itemize}
  \vspace*{1mm}
 }
 }
{\customcventry{Aug 2018 - May 2020}{Founder}{4ear}{Redlands, CA}{}
  {\begin{itemize}
    \item Startup focused on leveraging machine learning techniques on audio data to make insightful inferences. Primary focus was on performing better fault detection on internal combustion engines.   \vspace*{1mm}
  \end{itemize}
  }}
 


\section{RESEARCH}

{\customcvproject{Experimental Cosmology Lab -- University of California, Santa Barbara}{July 2017 - Sept 2019}
  {\begin{itemize}
    \item Lead researcher for the Experimental Cosmology Lab's Optical SETI team. Researched continuous-wave Optical SETI detection systems, specifically the software needed to make a cheap and robust system a reality.  \vspace*{1mm}
    \item Developed and maintained \texttt{OasisPy}, a software package written in Python designed to search astronomical images for transient sources of light that may be indicative of an incident optical signal from some extraterrestrial civilization.
  \end{itemize}
  }}
\vspace*{1mm}
{\customcvproject{Emory University Observatory -- Emory Department of Physics}{Sept 2016 – May 2018}
{\begin{itemize}
  \item As a student researcher working with PI Horace Dale, logged over 100 hours of observation time in Emory's in-house observatory. Duties included telescope programming and operation, data collection, and data processing.
\end{itemize}
}}

\section{EDUCATION}
{\customcventry{May 2018}{Bachelor of Science in Physics \& Astronomy: GPA 3.51}{Emory University}{Atlanta, GA}{}{}}

\section{SKILLS AND CERTIFICATIONS}

{\customcvproject{Technical Skills}{}
    {\begin{multicols}{4}
     \begin{itemize}
      \item Python
      \item TensorFlow
      \item Git
      \item HTML, CSS, Javascript
      \item SQL/PostgreSQL
      \item Snowflake/Sigma
      \item Swagger
      \item Postman
     \end{itemize}
     \end{multicols}}
     }
\vspace*{2.5mm} 
{\customcvproject{Agile Capabilities}{}
    {\begin{multicols}{4}
     \begin{itemize}
      \item SAFe methodologies
      \item Jira/Confluence
      \item Aha!
      \item SDLC
     \end{itemize}
     \end{multicols}}
     }
\vspace*{2.5mm} 
{\customcvproject{Certifications}{}
    {\begin{itemize}
        \vspace*{1mm}
        \item Certified SAFe PM/PO (completed in April 2022)
    \end{itemize}
    }


}
% Publications from a BibTeX file without multibib
%  for numerical labels: \renewcommand{\bibliographyitemlabel}{\@biblabel{\arabic{enumiv}}}% CONSIDER MERGING WITH PREAMBLE PART
%  to redefine the heading string ("Publications"): \renewcommand{\refname}{Articles}
\nocite{*}
\bibliographystyle{plain}
\bibliography{publications}                        % 'publications' is the name of a BibTeX file

% Publications from a BibTeX file using the multibib package
%\section{Publications}
%\nocitebook{book1,book2}
%\bibliographystylebook{plain}
%\bibliographybook{publications}                   % 'publications' is the name of a BibTeX file
%\nocitemisc{misc1,misc2,misc3}
%\bibliographystylemisc{plain}
%\bibliographymisc{publications}                   % 'publications' is the name of a BibTeX file

%-----       letter       ---------------------------------------------------------

\end{document}


%% end of file `template.tex'.
