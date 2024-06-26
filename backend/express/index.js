import express from "express";
import cors from "cors";
import ehrRouter from "./routes/EHRRoutes.js";
import dailyNewsLetterRouter from "./routes/DailyNewsLetterRoutes.js";
import reminderRouter from "./routes/ReminderRoutes.js";
import feedbackRouter from "./routes/FeedbackRoutes.js";
import alzheimerReportRouter from "./routes/AlzheimerReportRoutes.js";
import userRouter from "./routes/UserRoutes.js";
import adminRouter from "./routes/AdminRoutes.js";
import pneumoniaReportRouter from "./routes/PneumoniaReport.js"
import drugRouter from "./routes/DrugRoutes.js"
import appointmentRouter from "./routes/AppointmentRoutes.js"
import healthEducationRouter from "./routes/HealthEducationRoutes.js"
import fetalHealthReportRouter from './routes/FetalHealthReportRoutes.js'

const app = express();

app.use(express.json());
app.use(cors());

app.use("/admin", adminRouter);
app.use("/user", userRouter);
app.use("/ehr", ehrRouter);
app.use("/daily-newsletter", dailyNewsLetterRouter);
app.use("/reminder", reminderRouter);
app.use("/alzheimer-report", alzheimerReportRouter);
app.use("/feedback", feedbackRouter);
app.use("/pneumonia-report", pneumoniaReportRouter);
app.use("/fetal-report", fetalHealthReportRouter);
app.use("/drug", drugRouter)
app.use("/appointment", appointmentRouter)
app.use("/blog", healthEducationRouter)

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
