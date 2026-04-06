import React, { useState, useRef, useEffect } from "react";
import { researchApi } from "../config/congfiguration";

const ResearchBox: React.FC = () => {
   const [query, setQuery] = useState<string>("");
   const [result, setResult] = useState<string>("");

   const [plan, setPlan] = useState<any[]>([]);
   const [currentStep, setCurrentStep] = useState<string>("");

   const bottomRef = useRef<HTMLDivElement>(null);

   useEffect(() => {
      bottomRef.current?.scrollIntoView({ behavior: "smooth" });
   }, [result]);

   const handleResearch = async () => {
      if (!query.trim()) return;

      setResult("");
      setPlan([]);
      setCurrentStep("");

      try {
         const res = await researchApi(query);

         const taskId = res.task_id;
         setPlan(res.plan || []);
         console.log("Received plan:", res.plan);

         const socket = new WebSocket(`ws://127.0.0.1:8000/ws/${taskId}`);

         socket.onopen = () => {
            console.log("-- WebSocket connected --");
         };

         socket.onmessage = (event) => {
            if (event.data === "[DONE]") {
               socket.close();
               return;
            }

            if (event.data === "__ping__") return;

            try {
               const parsed = JSON.parse(event.data);

               if (parsed.type === "step") {
                  setCurrentStep(parsed.step);
                  return;
               }
            } catch {
               setResult((prev) => prev + event.data);
            }
         };

         socket.onerror = (err) => {
            console.error("WebSocket error:", err);
            setResult("Error in streaming");
         };

         socket.onclose = () => {
            console.log("--- WebSocket closed ---");
         };
      } catch (error) {
         console.error(error);
         setResult("API Error");
      }
   };

   return (
      <div className="flex h-screen w-full">

         <div className="flex flex-col w-4/5 bg-gray-900 text-white p-4 relative">

            <h2 className="text-xl font-bold text-center mb-2">
               Gas Town Multi-Agent Orchestration System
            </h2>

            {result && (
               <div className="flex-1 bg-gray-800 border border-gray-700 rounded-lg p-4 overflow-y-auto max-h-[87vh] custom-scrollbar">
                  <pre className="whitespace-pre-wrap wrap-break-words text-sm leading-relaxed">
                     {result}
                  </pre>
                  <div ref={bottomRef} />
               </div>
            )}

            {/* INPUT */}
            <div className="flex gap-3 absolute bottom-2 left-0 w-full px-4">
               <input
                  className="flex-1 bg-gray-800 border border-gray-600 text-white px-4 py-2 rounded-lg focus:outline-none hover:focus:ring-2 focus:ring-blue-500"
                  value={query}
                  onChange={(e) => setQuery(e.target.value)}
                  placeholder="Enter topic..."
               />

               <button
                  onClick={handleResearch}
                  className=" px-5 py-2 rounded-lg font-semibold border border-gray-600 focus:outline-none hover:focus:ring-2 focus:ring-blue-500"
               >
                  Send
               </button>
            </div>
         </div>

         <div className="w-1/5 bg-gray-950 text-white p-4 border-l border-gray-700">

            <h3 className="text-lg font-bold mb-4">Mayor Plan & Actions</h3>

            <div className="space-y-2">
               {plan.length > 0 ? (
                  plan.map((p, i) => (
                     <div
                        key={i}
                        className={`p-2 rounded-lg text-sm transition ${currentStep === p.type
                           ? "bg-green-600 font-bold"
                           : "bg-gray-800"
                           }`}
                     >
                        {p.type.toUpperCase()}
                     </div>
                  ))
               ) : (
                  <p className="text-gray-400 text-sm">No plan yet</p>
               )}
            </div>

            {currentStep && (
               <div className="mt-6">
                  <h4 className="text-md font-semibold mb-2">⚙️ Running</h4>
                  <div className="bg-blue-600 p-2 rounded-lg text-center">
                     {currentStep.toUpperCase()}
                  </div>
               </div>
            )}

            {plan.length > 0 && (
               <div className="mt-6">
                  <h4 className="text-sm mb-2">Progress</h4>
                  <div className="bg-gray-700 h-2 rounded">
                     <div
                        className="bg-green-500 h-2 rounded"
                        style={{
                           width: `${((plan.findIndex(p => p.type === currentStep) + 1) /
                              plan.length) *
                              100
                              }%`,
                        }}
                     />
                  </div>
               </div>
            )}

         </div>
      </div>
   );
};

export default ResearchBox;