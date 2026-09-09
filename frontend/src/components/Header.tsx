interface HeaderProps {
  onReset: () => void
  messageCount: number
}

export default function Header({ onReset, messageCount }: HeaderProps) {
  return (
    <header className="flex-shrink-0 bg-white border-b border-gray-100 px-6 py-4 flex items-center justify-between shadow-sm">
      <div className="flex items-center gap-3">
        <div className="w-10 h-10 bg-eco-600 rounded-xl flex items-center justify-center text-white text-xl shadow-sm">
          🌿
        </div>
        <div>
          <h1 className="font-bold text-gray-900 text-lg leading-none">EcoAssist</h1>
          <p className="text-xs text-gray-400 leading-none mt-0.5">
            AI Pollution &amp; Sustainability Guide
          </p>
        </div>
      </div>

      <div className="flex items-center gap-3">
        {/* SDG chips */}
        <div className="hidden sm:flex items-center gap-1">
          {['13', '11', '12', '3'].map(n => (
            <span
              key={n}
              className="text-xs font-bold px-2 py-0.5 rounded-full bg-eco-100 text-eco-700"
            >
              SDG {n}
            </span>
          ))}
        </div>

        {/* Reset button */}
        {messageCount > 0 && (
          <button
            onClick={onReset}
            title="New conversation"
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium
                       text-gray-500 hover:text-gray-700 hover:bg-gray-100 transition-all"
          >
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" className="w-3.5 h-3.5">
              <path fillRule="evenodd" d="M15.312 11.424a5.5 5.5 0 01-9.201 2.466l-.312-.311h2.433a.75.75 0 000-1.5H3.989a.75.75 0 00-.75.75v4.242a.75.75 0 001.5 0v-2.43l.31.31a7 7 0 0011.712-3.138.75.75 0 00-1.449-.39zm1.23-3.723a.75.75 0 00.219-.53V2.929a.75.75 0 00-1.5 0V5.36l-.31-.31A7 7 0 003.239 8.188a.75.75 0 101.448.389A5.5 5.5 0 0113.89 6.11l.311.31h-2.432a.75.75 0 000 1.5h4.243a.75.75 0 00.53-.219z" clipRule="evenodd" />
            </svg>
            New chat
          </button>
        )}
      </div>
    </header>
  )
}
